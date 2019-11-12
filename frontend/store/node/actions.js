export default {
  async getNodes ({ commit }) {
    await this.$axios
      .$get('https://service.test/api/node/public/current')
      .then((response) => {
        commit('SET_NODES', response)
      })
  }
}
