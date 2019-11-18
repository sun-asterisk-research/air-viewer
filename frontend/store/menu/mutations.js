export default {
  SET_STATUS_MOBILE (state) {
    state.isOpenMobileMenu = !state.isOpenMobileMenu
  },
  SET_CLOSE_MOBILE (state) {
    state.isOpenMobileMenu = false
  }
}
