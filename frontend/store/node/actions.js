export default {
  async getNodes ({ commit }) {
    let host = ''
    if (process.env.NUXT_APP_ENV === 'production') {
      host = 'http://backend.app'
    }
    await this.$axios
      .$get(`${host}/api/node/public/current`)
      .then((response) => {
        commit('SET_NODES', response)
      }).catch((err) => {
        console.log(err)
      })
  }
}
