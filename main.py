import pandas
import unidecode

def unaccent(original_string):
    return unidecode.unidecode(original_string)

def remove_time(original_string):
    return original_string[:-9]

if __name__ == "__main__":
    locations_raw = pandas.read_csv("locations.csv", sep='\t', header=None, names=[
        "ID_0",
        "ISO",
        "NAME_0",
        "ID_1",
        "NAME_1",
        "HASC_1",
        "CCN_1",
        "CCA_1",
        "TYPE_1",
        "ENGTYPE_1",
        "NL_NAME_1",
        "VARNAME_1",
        "MULTI_POLYGON"
    ])
    print(locations_raw.columns)
    print(locations_raw["VARNAME_1"])
    locations_bad_cols = [
        "ID_0",
        "ISO",
        "ID_1",
        "HASC_1",
        "CCN_1",
        "CCA_1",
        "TYPE_1",
        "ENGTYPE_1",
        "NL_NAME_1",
        "VARNAME_1"
    ]
    locations_munged = locations_raw.drop(locations_bad_cols, axis=1)
    locations_munged["NAME_1"] = locations_munged["NAME_1"].apply(unaccent)
    locations_munged.to_csv('locations-cleaned.csv', index=False)

    '''
    report_date,location,location_type,data_field,data_field_code,time_period,time_period_type,value,unit
    '''
    reports_raw = pandas.read_csv("all_reports.csv", sep=',', header=0, names=[
        "report_date",
        "location",
        "location_type",
        "data_field",
        "data_field_code",
        "time_period",
        "time_period_type",
        "value",
        "unit"
    ])
    print(reports_raw.head(5))
    reports_raw["location"] = reports_raw["location"].apply(unaccent)
    reports_raw["report_date"] = reports_raw["report_date"].apply(remove_time)
    print(reports_raw["report_date"])
    reports_raw.to_csv('all_reports-cleaned.csv', index=False)
