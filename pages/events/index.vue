<template>
  <Container>
    <span v-if="loading">
      Loading...
    </span>
    
    <div class="columns is-multiline is-mobile">
      <div v-for="item in events" :key="item.title" v-bind="item" class="column is-4">
        <div class="card">
          <div class="card-image">
            <figure class="image is-4by3">
              <a :href="`events/${item.id}/`"><img :src="item.image"  :alt="item.title"></a>
            </figure>
          </div>
          <div class="card-content">
            <div class="media">
              <div class="media-content">
                <p class="title is-4"><a :href="`events/${item.id}/`">{{ item.title }}</a></p>
                <p class="subtitle is-6">{{ formatDate(item.date) }}</p>
              </div>
            </div>

            <div class="content">
              <p>{{ item.excerpt }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </Container>
</template>

<script>
import Vue from 'vue'

import { buildUrl } from '../../utils/api'
import { formatDate } from '../../utils/date'

export default Vue.extend({
  data: () => ({
    loading: true,
    events: [],
  }),
  methods: {
    formatDate,
  },
  asyncData: async ({ $http }) => {
    const events = await $http.$get(buildUrl('events'))

    return {
      events,
      loading: false
    }
  }
})
</script>

