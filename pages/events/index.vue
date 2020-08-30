<template>
  <Container>
    <span v-if="loading">
      Loading...
    </span>
    <div v-for="item in events" :key="item.title" v-bind="item">
      {{ item.title }} - {{ item.date }}
    </div>
  </Container>
</template>

<script>
import Vue from 'vue'

import { buildUrl } from '../../utils/api'

export default Vue.extend({
  data: () => ({
    loading: true,
    events: [],
  }),
  asyncData: async ({ $http }) => {
    const events = await $http.$get(buildUrl('events'))
    return {
      events,
      loading: false
    }
  }
})
</script>

