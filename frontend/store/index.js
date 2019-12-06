export const state = () => ({
  locales: ['en', 'vi'],
  localeDefault: 'en'
})

export const getters = {
  isAuthenticated (state) {
    return state.auth.loggedIn
  },

  loggedInUser (state) {
    return state.auth.user
  }
}

export const mutations = {
  SET_LANG (state, locale) {
    if (state.locales.includes(locale)) {
      state.locale = locale
    }
  }
}

export const actions = {
  async nuxtServerInit ({ dispatch }) {
    await dispatch('node/getNodes')
  }
}
