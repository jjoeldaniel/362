import { redirect } from '@sveltejs/kit'

export const load = async ({ locals: { supabase, getSession } }) => {
  const session = await getSession()

  if (!session) {
    throw redirect(303, '/login')
  }

  const { data: profile } = await supabase
    .from('profiles')
    .select(`username, avatar_url, completions`)
    .eq('id', session.user.id)
    .single()

  return { session, profile }
}

