from googleapiclient import discovery
from googleapiclient.http import MediaFileUpload
from google.oauth2 import service_account
import gspread


class GDrive():
    def __init__(self, cred_obj):
        credentials = service_account.Credentials.from_service_account_info(
            cred_obj,
            scopes=['https://www.googleapis.com/auth/drive']
        )
        self.client = discovery.build('drive', 'v3', credentials=credentials)

    def mkdir(self, name, to):
        to = to.split('/')[-1]
        data = {
            'name': name,
            'mimeType': 'application/vnd.google-apps.folder',
            'parents': [to]
        }
        return self.client.files().create(body=data).execute()

    def copy(self, src_id, folder_id, name=None):
        data = {
            'parents': [folder_id],
        }
        if name:
            data['name'] = name
        return self.client.files().copy(fileId=src_id, body=data).execute()

    def rename(self, the_id, new_name):
        return self.client.files().update(fileId=the_id, body={'name': new_name}).execute()

    def upload(self, name, mimetype, local_path, to):
        return  # FIXME

    def untrash(self, the_id, folder_id):
        return self.client.files().update(fileId=the_id, addParents=folder_id).execute()


class GSheet():

    def __init__(self, cred_obj):
        credentials = service_account.Credentials.from_service_account_info(
            cred_obj,
            scopes=['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        )
        # you may pass your class which inheritent gspread.client.Client to gspread.authorize,
        # that subclass may overrides #departure and #request to impl your own rate control and exception handling (retry)
        self.cred_obj = cred_obj
        self.client = gspread.authorize(credentials)

    def create_spread_sheet(self, name, to, first_sheet_name=None):
        credentials = service_account.Credentials.from_service_account_info(
            self.cred_obj,
            scopes=['https://www.googleapis.com/auth/drive']
        )
        service = discovery.build('drive', 'v3', credentials=credentials)
        to = to.split('/')[-1]
        data = {
            'name': name,
            'mimeType': 'application/vnd.google-apps.spreadsheet',
            'parents': [to]
        }
        # doc: https://developers.google.com/drive/api/v3/reference/files/create
        ret = service.files().create(body=data, fields='*').execute()
        if first_sheet_name is not None:
            ss = self.client.open_by_key(ret['webViewLink'])
            ss.sheet1.update_title(first_sheet_name)
        return ret

    def export_sheet(self, key, save_path, export_format='xlsx'):
        save_path.write_bytes(
            self.client.request(
                'get',
                f'https://docs.google.com/spreadsheets/d/{key}/export',
                params={'format': export_format, 'id': key}
            ).content
        )

    def set_data_validation(self, key, sheet_name, condition, start_row_idx=None, end_row_idx=None, start_col_idx=None, end_col_idx=None, strict=True, dropdown=True, inputMessage=None):
        '''
        https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/request#setdatavalidationrequest
        https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/other#GridRange

        idx should be 0 based

        'condition': {
            'type': 'NUMBER_GREATER',
            'values': [{'userEnteredValue': '5'}]
        },
        '''
        wks = self.client.open_by_key(key)
        return wks.batch_update({
            'requests': [{
                'setDataValidation': {
                    'range': {
                        k: v for k, v in [
                            ('sheetId', wks.worksheet(sheet_name).id),
                            ('startRowIndex', start_row_idx),
                            ('endRowIndex', end_row_idx),
                            ('startColumnIndex', start_col_idx),
                            ('endColumnIndex', end_col_idx)
                        ] if v is not None
                    },
                    'rule': {
                        'condition': condition,
                        'inputMessage': inputMessage or '',
                        'showCustomUi': dropdown,
                        'strict': strict
                    }
                }
            }]
        })

    def import_img(self, sheet_id, sheet_name, row, col, cs_client, img_url=None, img_path=None, resize_width=1280, resize_height=720):
        return  # FIXME set the corresponding cell to f'=IMAGE({img_url})'

    def get_sheet(self, key, sheet_name):
        return self.client.open_by_key(key).worksheet(sheet_name).get_all_values()
