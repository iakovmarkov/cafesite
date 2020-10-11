<template>
  <Container>
    <span v-if="loading">
      Loading...
    </span>
    <div class="columns" v-for="category in categories" :key="category.key" v-bind="category">
      <div class="column is-half is-offset-one-quarter">
        <h4 class="title">{{ category.key }}</h4>
        <div v-for="item in category.value" :key="item.title" v-bind="item" class="my-4">
          <div class="menu-item">
            <div class="text">
              <span class="name">{{ item.title }}</span>
              <div class="description">{{ item.description }}</div>
            </div>
            <div class="price">{{ item.price }} CZK</div>
          </div>
        </div>
      </div>
    </div>
    
  </Container>
</template>

<script>
import Vue from 'vue'
import { buildUrl } from '../utils/api'
import * as r from 'ramda'

export default Vue.extend({
  data: () => ({
    loading: true,
    menu: [],
  }),

  computed: {
    categories: ({ menu }) => {
      return r.pipe(
        r.groupBy(item => item.category),
        r.toPairs(),
        r.map(([key, value]) => ({ key, value }))
      )(menu)
    }
  },

  asyncData: async ({ $http }) => {
    const menu = await $http.$get(buildUrl('menu'))

    return {
      menu,
      loading: false
    }
  }
})
</script>