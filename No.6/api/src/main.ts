import { request } from './types/request'
import { response } from './types/response'
import { controller } from './controller'

function doPost(e: any): GoogleAppsScript.Content.TextOutput {
  const req: request = JSON.parse(e.postData.contents)
  const res: response = controller(req)

  return createResponse(res)
}

function createResponse(data: object): GoogleAppsScript.Content.TextOutput {
  return ContentService.createTextOutput(JSON.stringify(data)).setMimeType(ContentService.MimeType.JSON)
}
