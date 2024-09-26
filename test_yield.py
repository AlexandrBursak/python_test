from bson import ObjectId


# status = 'something'
# def get_status():
#     status = ['COLOR_GONE', 'COMPLITED']
#     for :
#         yield status

def add_job(item):
    print(item)


status = [
    {
        'color': 'blue',
        'status': 'COLOR_GONE'

    }, 
    {
        'color': 'green',
        'status': 'COMPLETED'
    }
]
job_id=ObjectId()
jp_records = [
    {
        'job_id': job_id,
        'pid': ObjectId(),
        'uid': ObjectId(),
        'qid': 10,
        'queue_type': '',
        'payload': '{}',
        'use_kubeworkers': False,
        'color': item.get('color'),
        'status': item.get('status')
    }
    for item in status
]

for job_process in jp_records:
    add_job(job_process)

print(jp_records)