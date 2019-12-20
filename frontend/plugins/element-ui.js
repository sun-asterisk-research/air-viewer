import Vue from 'vue'

import locale from 'element-ui/lib/locale'
import langEn from 'element-ui/lib/locale/lang/en'

import Table from 'element-ui/lib/table'
import TableColumn from 'element-ui/lib/table-column'

import Carousel from 'element-ui/lib/carousel'
import CarouselItem from 'element-ui/lib/carousel-item'

import Button from 'element-ui/lib/button'
import Card from 'element-ui/lib/card'
import Tooltip from 'element-ui/lib/tooltip'

export default function () {
  locale.use(langEn)

  Vue.component('ElTable', Table)
  Vue.component('ElTableColumn', TableColumn)

  Vue.component('ElCarousel', Carousel)
  Vue.component('ElCarouselItem', CarouselItem)

  Vue.component('ElButton', Button)
  Vue.component('ElCard', Card)
  Vue.component('ElTooltip', Tooltip)
}
