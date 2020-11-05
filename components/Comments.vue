<template>
  <div>
    <div class="card my-2" v-for="comment in comments" :key="comment.id" v-bind="comment">
      <div class="card-content comment">
        <p class="meta">{{ comment.name }} ({{ comment.email }}) on {{ formatDate(comment.date) }}:</p>
        <div class="content">
          {{ comment.text }}
        </div>
      </div>
    </div>
    <progress v-if="loading" class="progress is-info" max="100"></progress>
    <div class="card my-2 px-3 py-3">
      <form @submit.prevent="handleSubmit">
        <div class="field">
          <div class="control">
            <input class="input" type="text" placeholder="John Doe" v-model="formData.name">
          </div>

          <p v-if="errors.name">
            <p class="help is-danger" v-for="error in errors.name" :key="error">{{ error }}</p>
          </p>
        </div>

        <div class="field">
          <div class="control">
            <input class="input" type="email" placeholder="hi@cafe.com" v-model="formData.email">
          </div>

          <p v-if="errors.email">
            <p class="help is-danger" v-for="error in errors.email" :key="error">{{ error }}</p>
          </p>
        </div>

        <div class="field">
          <div class="control">
            <textarea class="textarea" placeholder="Write something..." v-model="formData.text"></textarea>
          </div>

          <p v-if="errors.text">
            <p class="help is-danger" v-for="error in errors.text" :key="error">{{ error }}</p>
          </p>
        </div>

        <div class="field is-grouped">
          <div class="control">
            <button class="button is-link" type="submit">Submit</button>
          </div>
        </div>

        <div class="" v-if="submitting">Sending...</div>
        <div class="notification is-success" v-if="submitSuccess">
          <button class="delete" @click="hideSubmitStatus"></button>
          Your message has been sent sucessfully.
        </div>
        <div class="notification is-danger" v-if="submitError">
          <button class="delete" @click="hideSubmitStatus"></button>
          Couldn't send your message. Please, try again.
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import Vue from 'vue'
import validate from 'validate.js'
import * as r from 'ramda'
import { buildUrl } from '../utils/api'
import { formatDate } from '../utils/date'
import { mapActions } from 'vuex'

const constraints = {
  name: {
    presence: true,
    length: {
      minimum: 3,
    }
  },
  email: {
    presence: true,
    email: true,
  },
  text: {
    presence: true,
    length: {
      minimum: 3,
    }
  }
}

export default Vue.extend({
  props: ['id'],
  data() {
    return {
      formData: {},
      errors: {},
      submitting: false,
      submitError: false,
      submitSuccess: false,
    };
  },
  methods: {
    ...mapActions('comments', ['loadComments', 'postComment']),
    formatDate,
    handleSubmit: async function(e) {
      this.errors = validate(
        this.formData,
        constraints
      ) || {}

      if (r.length(r.keys(this.errors)) > 0) {
        return
      }

      this.submitSuccess = false
      this.submitting = true

      try {
        await this.postComment({
          comment: this.formData,
          id: this.id
        })
        this.submitError = undefined
        this.submitSuccess = true
        this.formData = {}
      } catch (e) {
        console.error(e);
        this.submitError = e
        this.submitSuccess = false
      }

      this.submitting = false
    },
    hideSubmitStatus() {
      this.submitError = undefined
      this.submitSuccess = false
      this.submitting = false
    },
  },
  mounted() {
    this.loadComments({ id: this.id });
  },
  computed: {
    loading() {
      return this.$store.state.comments.loading
    },
    comments() {
      console.warn(this.$store.state.comments);
      console.warn(this.$store.state.comments.comments[this.id]);
      return this.$store.state.comments.comments[this.id] || {}
    },
  },
})
</script>

