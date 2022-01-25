import { getLoginSession } from '../../lib/auth'
import { findUser } from '../../lib/user'
import {dbConnect} from '../../lib/db_connection_inoperative';
export default async function user(req, res) {
  try {
    if (!global.mongoose) {
      await dbConnect();

    }
    const session = await getLoginSession(req)
    const user = (session && (await findUser(session))) ?? null

    res.status(200).json({ user })
  } catch (error) {
    console.error(error)
    res.status(500).end('Authentication token is invalid, please log in')
  }
}
