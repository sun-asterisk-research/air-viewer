export default {
  async getNodes ({ commit }) {
    await this.$axios
      .$get('/api/node/public/current')
      .then((response) => {
        commit('SET_NODES', response)
      }).catch((err) => {
        console.log(err)
      })
  }
}
