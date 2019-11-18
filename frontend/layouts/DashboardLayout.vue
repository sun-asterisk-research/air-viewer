<template>
  <div id="wrapper" :class="wrapperClass">
    <MenuToggleBtn />

    <Menu />

    <ContentOverlay />
    <div style="position: relative; margin-left: -20px;">
      <base-nav type="default" effect="dark" expand>
        <div slot="content-header" slot-scope="{closeMenu}" class="row">
          <div class="col-6 collapse-brand">
            <nuxt-link to="/">
              <img src="~/static/argon/img/brand/blue.png">
            </nuxt-link>
          </div>
          <div class="col-6 collapse-close">
            <close-button @click="closeMenu" />
          </div>
        </div>

        <ul class="navbar-nav ml-lg-auto">
          <li class="nav-item">
            <a class="nav-link nav-link-icon" href="#">
              Discover
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link nav-link-icon" href="#">
              Profile
            </a>
          </li>
          <base-dropdown tag="li" title="Settings">
            <a class="dropdown-item" href="#">Action</a>
            <a class="dropdown-item" href="#">Another action</a>
            <a class="dropdown-item" href="#">Something else here</a>
            <div class="dropdown-divider" />
            <a class="dropdown-item" href="#">Separated link</a>
          </base-dropdown>
        </ul>
      </base-nav>
    </div>
    <main>
      <nuxt />
    </main>
  </div>
</template>
<script>
import { mapState } from 'vuex'
const BaseNav = () => import('@/components/argon/BaseNav')
const BaseDropdown = () => import('@/components/argon/BaseDropdown')
const MenuToggleBtn = () => import('@/components/Menu/MenuToggleBtn')
const Menu = () => import('@/components/Menu/Menu')
const ContentOverlay = () => import('@/components/Menu/ContentOverlay')
const CloseButton = () => import('@/components/argon/CloseButton')

export default {
  components: {
    MenuToggleBtn,
    Menu,
    ContentOverlay,
    BaseNav,
    BaseDropdown,
    CloseButton
  },
  computed: {
    ...mapState('menu', {
      toggleMenu: 'isOpenMobileMenu'
    }),
    wrapperClass () {
      return {
        'toggled': this.toggleMenu === true
      }
    }
  }
}
</script>
<style lang="scss" scoped>
@import '~/assets/sidebar/layout.scss';
@import '~/assets/sidebar/media-queries.scss';
</style>
