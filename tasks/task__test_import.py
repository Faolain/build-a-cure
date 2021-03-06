from sanitize import json_to_csv
from import_elk import import_to_elk

messages = []
params = {}
params['index_name'] = 'fgt_event'
params['data_path'] = '/data/test/'
params['es_host'] = 'localhost'
converted = json_to_csv(params['data_path'])
if converted:
	imported = import_to_elk(params)
	if imported:
		messages.append(''.join(['finished importing', str(imported)]))
		es = connect_to_es(params['es_host'])
		if es:
			res = search_entries(es, None, params['index_name'], None)
			if res:
				messages.append(''.join(['retrieved results', str(res['hits']['total']['value'])]))
				for hit in res['hits']['hits']:
					messages.append('\n'.join([','.join([k, '::', v]) for k, v in hit.items()]))
		if len(messages) > 0:
			open('messages.txt', 'w').write('\n'.join(messages))