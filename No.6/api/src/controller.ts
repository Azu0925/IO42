import { request } from './types/request'
import { response } from './types/response'
import { uploadDrive } from './uploadDrive'

export const controller = (req: request): response => {
  const fileData = base64Decode(req.content)
  const url = uploadDrive(fileData, req.name)
  const res: response = {
    url: url,
  }

  return res
}

function base64Decode(data: string): Buffer {
  const fileData = data.replace(/^data:\w+\/\w+;base64,/, '')
  return new Buffer(fileData, 'base64')
}
