export default {
  toggle ({ commit }) {
    commit('SET_STATUS_MOBILE')
  },
  closeMobileMenu ({ commit }) {
    commit('SET_CLOSE_MOBILE')
  }
}
