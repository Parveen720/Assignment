from pyspark.sql.functions import col

# Load metadata table
df = spark.table("assignment.metadata")

# Extract possible table type prefixes (e.g., Raw, Curated, Presentation)
table_types = {
    col_name.replace("TableName", "").strip()
    for col_name in df.columns
    if "TableName" in col_name and col_name.replace("TableName", "").strip()
}

# Iterate over each table type
for t_type in table_types:
    table_col = f"{t_type}TableName"
    column_col = f"{t_type}TableColumn"
    datatype_col = f"{t_type}TableColumnDatatype"

    # Get all unique table names for this type
    unique_tables = (
        df.select(table_col)
          .where(col(table_col).isNotNull())
          .distinct()
          .rdd.flatMap(lambda x: x)
          .collect()
    )

    for tbl in unique_tables:
        # Filter relevant rows for this table
        columns_df = (
            df.filter(col(table_col) == tbl)
              .select(column_col, datatype_col)
              .dropna()
              .distinct()
        )

        # Build SQL column definitions
        column_definitions = ",\n  ".join(
            [f"`{row[column_col]}` {row[datatype_col]}" for row in columns_df.collect()]
        )

        full_table_name = f"{t_type}_{tbl}"

        # Drop if exists
        spark.sql(f"DROP TABLE IF EXISTS assignment.`{full_table_name}`")

        # Create new table
        create_query = f"""
        CREATE TABLE assignment.`{full_table_name}` (
          {column_definitions}
        )
        """
        print(f"Creating table: assignment.{full_table_name}")
        spark.sql(create_query)
