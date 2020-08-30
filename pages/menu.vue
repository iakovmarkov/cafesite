<template>
  <Container>
    <span v-if="loading">
      Loading...
    </span>
    <div v-for="item in menu" :key="item.title" v-bind="item">
      {{ item.title }} - {{ item.price }}
    </div>
  </Container>
</template>

<script>
import Vue from 'vue'
import { buildUrl } from '../utils/api'

export default Vue.extend({
  data: () => ({
    loading: true,
    menu: [],
  }),
  asyncData: async ({ $http }) => {
    const menu = await $http.$get(buildUrl('menu'))
    return {
      menu,
      loading: false
    }
  }
})
</script>