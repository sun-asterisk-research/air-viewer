export default {
  async getNodes ({ commit }) {
    let host = ''
    if (process.env.NUXT_APP_ENV === 'production') {
      host = process.env.BACKEND_HOST
    }
    await this.$axios
      .$get(`${host}/api/node/public/current`)
      .then((response) => {
        commit('SET_NODES', response)
      }).catch((err) => {
        console.log(err)
      })
  },

  async registerNode ({ commit }, params) {
    await this.$axios
      .$post('/api/node', params)
      .then((response) => {
        this.$toast.success(response.message)
        this.$router.push('/admin/node/list-nodes')
      })
      .catch((err) => {
        this.$toast.error(err.message)
      })
  },

  async editNode ({ commit }, params) {
    await this.$axios
      .$post(`/api/node/${params.id}`, params)
      .then((response) => {
        this.$toast.success(response.message)
        this.$router.push('/admin/node/list-nodes')
      })
      .catch((err) => {
        this.$toast.error(err.message)
      })
  },

  async deleteNode ({ commit }, id) {
    await this.$axios
      .$delete(`/api/node/${id}`)
      .then((response) => {
        this.$toast.success(response.message)
      })
      .catch((err) => {
        this.$toast.error(err.message)
      })
  }
}
