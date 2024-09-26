
setup_val = [
	(True, True),
	(True, False),
	(False, True),
	(False, False),
] 

for i, j in setup_val:
	trial_user = i
	is_serverside_batchscoring_self_service_enabled = j

	result_cond = not (trial_user or is_serverside_batchscoring_self_service_enabled)

	print('trial_user:', trial_user)
	print('is_serverside_batchscoring_self_service_enabled:', is_serverside_batchscoring_self_service_enabled)
	print('result_cond:', result_cond)