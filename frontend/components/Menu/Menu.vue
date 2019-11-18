<template>
  <div class="menu-container">
    <!-- root level itens -->
    <ul class="menu">
      <li class="menu__top">
        <nuxt-link to="/" class="menu__logo">
          <img src="~/static/argon/img/brand/white.png" style="width: 200px;" alt="icon">
        </nuxt-link>
      </li>

      <li>
        <a
          href="#"
          :class="highlightSection('home')"
          @click.prevent="updateMenu('home')"
        >
          <i class="fa fa-home menu__icon" aria-hidden="true" />
          Home
        </a>
      </li>

      <li>
        <a
          href="#"
          :class="highlightSection('products')"
          @click.prevent="updateMenu('products')"
        >
          <i class="fa fa-tag menu__icon" aria-hidden="true" />
          Products
          <i class="fa fa-chevron-right menu__arrow-icon" aria-hidden="true" />
        </a>
      </li>

      <li>
        <a
          href="#"
          :class="highlightSection('customers')"
          @click.prevent="updateMenu('customers')"
        >
          <i class="fa fa-users menu__icon" aria-hidden="true" />
          Customers
          <i class="fa fa-chevron-right menu__arrow-icon" aria-hidden="true" />
        </a>
      </li>

      <li>
        <a
          href="#"
          :class="highlightSection('account')"
          @click.prevent="updateMenu('account')"
        >
          <i class="fa fa-user menu__icon" aria-hidden="true" />
          Account
          <i class="fa fa-chevron-right menu__arrow-icon" aria-hidden="true" />
        </a>
      </li>
    </ul>

    <!-- context menu: childs of root level itens -->
    <transition name="slide-fade">
      <div v-show="showContextMenu" class="context-menu-container">
        <ul class="context-menu">
          <li v-for="(item, index) in menuItens" :key="index">
            <h5 v-if="item.type === 'title'" class="context-menu__title">
              <i :class="item.icon" aria-hidden="true" />

              {{ item.txt }}

              <a
                v-if="index === 0"
                class="context-menu__btn-close"
                href="#"
                @click.prevent="closeContextMenu"
              >
                <i class="fa fa-window-close" aria-hidden="true" />
              </a>
            </h5>

            <a
              v-else
              href="#"
              :class="subMenuClass(item.txt)"
              @click.prevent="openSection(item)"
            >
              {{ item.txt }}
            </a>
          </li>
        </ul>
      </div>
    </transition>
  </div>
</template>

<script>
import kebabCase from 'lodash/kebabCase'
import menuData from './support/menu-data'

export default {
  name: 'Menu',
  data () {
    return {
      contextSection: '',
      menuItens: [],
      menuData,
      activeSubMenu: ''
    }
  },
  computed: {
    showContextMenu () {
      return this.menuItens.length
    }
  },
  methods: {
    openProjectLink () {
      alert('You could open the project frontend in another tab here, so the logged admin could see changes made to the project ;)')
    },
    updateMenu (context) {
      this.contextSection = context
      this.menuItens = this.menuData[context]
      if (context === 'home') {
        this.$router.push('/')
        this.$store.dispatch('menu/closeMobileMenu')
      }
    },
    highlightSection (section) {
      return {
        'menu__link': true,
        'menu__link--active': section === this.contextSection
      }
    },
    subMenuClass (subMenuName) {
      return {
        'context-menu__link': true,
        'context-menu__link--active': this.activeSubMenu === subMenuName
      }
    },
    closeContextMenu () {
      this.contextSection = ''
      this.menuItens = []
    },
    openSection (item) {
      this.activeSubMenu = item.txt
      this.$router.push(this.getUrl(item))
      this.$store.dispatch('menu/closeMobileMenu')
    },
    getUrl (item) {
      const sectionSlug = kebabCase(item.txt)
      return `${item.link}/${sectionSlug}`
    }
  }
}
</script>
<style lang="scss">
@import '~/assets/sidebar/menu.scss';
</style>
