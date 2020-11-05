<template>
  <div>
    <span v-if="loading">Loading...</span>

    <div v-if="item">
      <section
        class="hero is-image is-dark is-large"
        :style="`background-image: url(${item.image});`"
      >
        <div class="hero-body">
          <div class="container">
            <p class="title">{{ item.title }}</p>
          </div>
        </div>
      </section>
      <Container>
        <div class="columns my-5">
          <div class="column is-8">
            <div class="block"><p>{{ item.description }}</p></div>
          </div>
          <div class="column is-4">
            <h5 class="title">{{ date }}</h5>
            <h6 class="subtitle">When</h6>
            <h5 class="title">Cafe, main stage</h5>
            <h6 class="subtitle">Where</h6>
          </div>
        </div>
        <div class="columns my-5">
          <div class="column is-half">
            <Comments :id="id" />
          </div>
        </div>
      </Container>
    </div>
  </div>
</template>

<script>
import Vue from 'vue'

import { buildUrl } from '../../utils/api'
import { formatDate } from '../../utils/date'

export default Vue.extend({
  data: () => ({
    loading: true,
    event: null,
  }),
  computed: {
    date: ({ item }) => formatDate(item.date),
    id: ({ $route }) => $route.params.id,
  },
  async asyncData({ $http, params }) {
    const event = await $http.$get(buildUrl('events', params.id))
    return {
      item: event,
      loading: false,
    }
  },
})
</script>

