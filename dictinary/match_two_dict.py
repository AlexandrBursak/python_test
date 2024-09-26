import json

output_schema=[
	(b'readmitted_True_PREDICTION', 'N'), 
	(b'readmitted_False_PREDICTION', 'N'), 
	(b'readmitted_PREDICTION', 'T'), 
	(b'THRESHOLD', 'N'), 
	(b'POSITIVE_CLASS', 'T'), 
	(b'race', 'T'), 
	(b'gender', 'T'), 
	(b'age', 'T'), 
	(b'weight', 'T'), 
	(b'admission_type_id', 'T'), 
	(b'discharge_disposition_id', 'T'), 
	(b'admission_source_id', 'T'), 
	(b'time_in_hospital', 'T'), 
	(b'payer_code', 'T'), 
	(b'medical_specialty', 'T'), 
	(b'num_lab_procedures', 'T'), 
	(b'num_procedures', 'T'), 
	(b'num_medications', 'T'), 
	(b'number_outpatient', 'T'), 
	(b'number_emergency', 'T'), 
	(b'number_inpatient', 'T'), 
	(b'diag_1', 'T'), 
	(b'diag_2', 'T'), 
	(b'diag_3', 'T'), 
	(b'number_diagnoses', 'T'), 
	(b'max_glu_serum', 'T'), 
	(b'A1Cresult', 'T'), 
	(b'metformin', 'T'), 
	(b'repaglinide', 'T'), 
	(b'nateglinide', 'T'), 
	(b'chlorpropamide', 'T'), 
	(b'glimepiride', 'T'), 
	(b'acetohexamide', 'T'), 
	(b'glipizide', 'T'), 
	(b'glyburide', 'T'), 
	(b'tolbutamide', 'T'), 
	(b'pioglitazone', 'T'), 
	(b'rosiglitazone', 'T'), 
	(b'acarbose', 'T'), 
	(b'miglitol', 'T'), 
	(b'troglitazone', 'T'), 
	(b'tolazamide', 'T'), 
	(b'diag_1_desc', 'T'), 
	(b'diag_2_desc', 'T'), 
	(b'diag_3_desc', 'T')
]

string_json = '{"diag_3_desc": "readmitted_False_PREDICTION", "foobar": "burik", "foo": "bar"}'
remap_column = json.loads(string_json)
schema_list = set( items[0] for items in output_schema )
unavailable_column = set( items for items in remap_column if items.encode('utf-8') not in schema_list )


print("output_schema:", output_schema)
print("schema_list:", schema_list)

print("remap_column:", unavailable_column)

if len(unavailable_column) > 0:
	print('Some field is not available')
else:
	print('All is good')

