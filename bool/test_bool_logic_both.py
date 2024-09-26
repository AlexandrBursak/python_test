
def oposite_result(requires_lrs, is_external, allow_custom_models, allow_external_models):
	return (requires_lrs and not allow_custom_models) or (
        is_external and not allow_external_models
    )

def original_result(requires_lrs, is_external, allow_custom_models, allow_external_models):
	return (
	    not (requires_lrs or is_external)
	    or (requires_lrs and allow_custom_models)
	    or (is_external and allow_external_models)
	)

for requires_lrs, is_external, allow_custom_models, allow_external_models in (
	# [False, False, False, False],
	# [False, False, False, True],
	# [False, False, True, True],
	[False, True, True, True],
	# [True, True, True, True],
	[True, False, False, False],
	# [True, True, False, False],
	# [True, True, True, False],
	[True, False, True, False],
	[False, True, False, True],
	[False, True, False, False],
	# [False, False, True, False],
	[True, False, True, True],
	# [True, True, False, True],
):

	print('oposite_result', oposite_result(requires_lrs, is_external, allow_custom_models, allow_external_models))
	print('original_result', original_result(requires_lrs, is_external, allow_custom_models, allow_external_models))
	print('requires_lrs, is_external, allow_custom_models, allow_external_models', requires_lrs, is_external, allow_custom_models, allow_external_models)
	print('-----------------------------')
