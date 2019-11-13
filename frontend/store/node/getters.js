
export default {
  nodeDetail: (state) => {
    return id => state.nodes.nodes.filter((item) => {
      return item.id === Number(id)
    })
  }
}
