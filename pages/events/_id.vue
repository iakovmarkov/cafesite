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
        <div class="columns">
          <div class="column is-8">
            <div class="block"><p>{{ item.description }}</p></div>
          </div>
          <div class="column is-4">
            <h5 class="title">{{ item.date }}</h5>
            <h6 class="subtitle">When</h6>
            <h5 class="title">Cafe</h5>
            <h6 class="subtitle">Where</h6>
            <div class="buttons">
              <button class="button is-primary">Book online</button>
              <a class="button is-white" href="tel:+420604779221">Call us</a>
            </div>
          </div>
        </div>
      </Container>
    </div>
  </div>
</template>

<script>
import Vue from 'vue'

import { buildUrl } from '../../utils/api'

export default Vue.extend({
  data: () => ({
    loading: true,
    event: null,
  }),
  asyncData: async ({ $http, params }) => {
    const event = await $http.$get(buildUrl('events', params.id))
    return {
      item: event,
      loading: false,
    }
  },
})
</script>

