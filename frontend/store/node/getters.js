
export default {
  getNodes: (state) => {
    return state.nodes.nodes.filter((item) => {
      return item.data !== ''
    })
  },
  nodeDetail: (state) => {
    return id => state.nodes.nodes.filter((item) => {
      return item.id === Number(id)
    })
  }
}
