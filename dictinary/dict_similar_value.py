col = 'diag.1'
sanitazed = 'diag_1'
sanitazed_names = {
    'admission_type_id': 'admission_type_id',
    'age': 'age',
    'diag$1': 'diag_1',
    'diag.1': 'diag_1',
    'gender': 'gender',
    'medical_specialty': 'medical_specialty',
    'payer_code': 'payer_code',
    'race': 'race'
}

print('Set dict:', sanitazed_names)

similar_col_name = [k for k, v in sanitazed_names.items() if v == sanitazed]

print('Similar dict:', similar_col_name[0], similar_col_name[1])