import Vue from 'vue'
import VueLazyload from 'vue-lazyload'
import vClickOutside from 'v-click-outside'
import globalComponents from './globalComponents'
import globalDirectives from './globalDirectives'

Vue.use(globalComponents)
Vue.use(globalDirectives)
Vue.use(VueLazyload)
// Replace custom click-outside directive with vClickOutside (IOS fix)
Vue.use(vClickOutside)
