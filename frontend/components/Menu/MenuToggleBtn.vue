<template>
  <a
    href="#"
    class="btn menu-toggle-btn"
    @click.prevent="toggleMenu"
  >
    <i class="fa fa-bars" aria-hidden="true" />
  </a>
</template>

<script>
import { mapActions } from 'vuex'
export default {
  methods: {
    ...mapActions('menu', {
      toggleMenu: 'toggle'
    })
  }
}
</script>
<style lang="scss">
.menu-toggle-btn {
  display: block;
  position: fixed;
  top: 10px;
  left: 15px;
  z-index: 1001;
  color: #0078bd;
  border-color: #ebeef0;
  background: #fff;
}
</style>
