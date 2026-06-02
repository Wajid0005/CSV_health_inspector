from loader import load_data
class CSVInspector:

    def __init__(self, data):
        self.data = data
        self.rows, self.cols = data.shape


    def check_shape(self):
        shape_out = f"✓ Shape: {self.rows} rows, {self.cols} columns"
        return shape_out


    def check_missing(self):
        missing = self.data.isna().sum()
        na_list = [f"{col}({round((val / self.rows) * 100, 3)}%)" for col, val in missing.items() if val > 0]
        na_out = f"✓ Missing values: {', '.join(na_list) if na_list else 'None'}"
        return na_out

    def check_duplicates(self):
        duplicate = f"✓ Duplicates: {self.data.duplicated().sum()} rows"
        return duplicate

    def check_dtypes(self):
        num_count = self.data.select_dtypes(include=['number']).shape[1]
        cat_count = self.data.select_dtypes(exclude=['number']).shape[1]
        dtype_out = f"✓ Dtypes: {num_count} numeric, {cat_count} categorical"
        return dtype_out

    def check_suspicious_values(self):
        missing = self.data.isna().sum()

        sus_list = [
            f"{col}({val}rows are null)" for col, val in missing.items() if val > (self.rows // 4)]
        sus_out = f"✓ Suspicious values: {', '.join(sus_list) if sus_list else 'None'}"
        return  sus_out

    def generate_report(self):
        report = [self.check_shape(),
                  self.check_missing(),
                  self.check_duplicates(),
                  self.check_dtypes(),
                  self.check_suspicious_values()]
        return "\n".join(report)