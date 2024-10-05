from bson import ObjectId

job = {
    '_output_settings': {
        'type': 'local_file'
    },
    'abort_on_error': True,
    'aborted': None,
    'aborted_by': None,
    'batch_job_type': 'prediction',
    'batch_prediction_job_definition': None,
    'chunk_size': 'auto',
    'column_names_remapping': None,
    'completed': '2023, 7, 20, 11, 16, 40, 453000',
    'created': '2023, 7, 20, 11, 16, 25, 138000',
    'created_by': ObjectId('646b6f54ea0eb7d22cd319cb'),
    'csv_settings': {
        'delimiter': ',', 'encoding': 'utf-8', 'quotechar': '"'
    },
    'dataset_id': None,
    'dependent_jobs_ids': [],
    'deployment_id': ObjectId('64776856e4ea3618e67fd9ac'),
    'disable_row_level_error_handling': False,
    'explanation_algorithm': None,
    'explanation_class_names': None,
    'explanation_num_top_classes': None,
    'failed': None,
    'failed_rows': 0,
    'failed_rows_size': 0,
    'filename': None,
    'hidden': None,
    'hidden_by': None,
    'id': ObjectId('64b917898fa16f941dfc8d4d'),
    'include_prediction_status': False,
    'include_probabilities': True,
    'include_probabilities_classes': [],
    'instance_key': ObjectId('eb05433dc1da9a0b00bc7248'),
    'intake_dataset_display_name': '10k_diabetes.csv',
    'intake_settings': {
        'dataset_id': ObjectId('6487399c927f6b4d8fd24b60'),
        'type': 'dataset'
    },
    'job_intake_size': 3721878,
    'job_output_size': 4127487,
    'job_qid': '25',
    'log': [
        [
            '2023, 7, 20, 11, 16, 40, 453000',
            'Job created by {username}',
            {
                'username': 'alex.bursak@datarobot.com'
            },
            'INFO'
        ], [
            '2023, 7, 20, 11, 16, 40, 453000',
            'Job started processing',
            'INFO'
        ], [
            '2023, 7, 20, 11, 16, 40, 453000',
            'Job done processing',
            'INFO'
        ], [
            '2023, 7, 20, 11, 16, 40, 453000',
            'Results download started by {username}',
            {'username': 'alex.bursak@datarobot.com'},
            'INFO'
        ], [
            '2023, 7, 20, 11, 16, 40, 453000',
            'Results download started by {username}',
            {'username': 'alex.bursak@datarobot.com'},
            'INFO'
        ]
    ],
    'lrs_id': None,
    'max_explanations': 0,
    'max_ngram_explanations': None,
    'model_id': ObjectId('646bee6ba8fcc6a9d29c741c'),
    'monitoring_aggregation': None,
    'monitoring_batch_prefix': None,
    'monitoring_columns': None,
    'monitoring_output_settings': None,
    'num_concurrent': 4,
    'org_id': ObjectId('57eb3347d75f1670ebc5c4bd'),
    'passthrough_columns': None,
    'passthrough_columns_set': 'all',
    'prediction_environment_id': None,
    'prediction_instance': {
        'datarobot_key': 'b52759ee-4723-4a7a-37b1-12414c384f09',
        'host_name': '192.168.31.12',
        'ssl_enabled': False
    },
    'prediction_intervals_size': None,
    'prediction_warning_enabled': False,
    'preview_available': False,
    'project_id': ObjectId('646bec3832ca3b67b4ba20ae'),
    'results_deleted': False,
    'scored_rows': 10000,
    'skip_association_id_check': False,
    'skip_drift_tracking': False,
    'skipped_rows': 0,
    'source': 'ui_make_prediction',
    'started': '2023, 7, 20, 11, 16, 40, 453000',
    'status': 'COMPLETED',
    'status_id': None,
    'table_header': [],
    'threshold_high': None,
    'threshold_low': None,
    'timeseries_settings': {
        'is_time_series': False
    },
    'total_rows': 10000,
    'uploaded': None,
    'uploaded_chunks': 0,
    'user_scheduled_job_id': None,
    'writer_status': {
        'stored_chunks': 16
    }
}

print(job.csv_settings.get('encoding', 'utf-8'))
