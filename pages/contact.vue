<template>
  <Container>
    <div class="columns">
      <div class="column is-offset-one-quarter is-half">
        <form @submit.prevent="handleSubmit">
          <div class="field">
            <label class="label">Your name</label>
            <div class="control">
              <input class="input" type="text" placeholder="John Doe" v-model="formData.name">
            </div>

            <p v-if="errors.name">
              <p class="help is-danger" v-for="error in errors.name" :key="error">{{ error }}</p>
            </p>
          </div>

          <div class="field">
            <label class="label">Your Email</label>
            <div class="control">
              <input class="input" type="email" placeholder="hi@cafe.com" v-model="formData.email">
            </div>

            <p v-if="errors.email">
              <p class="help is-danger" v-for="error in errors.email" :key="error">{{ error }}</p>
            </p>
          </div>

          <div class="field">
            <label class="label">Subject</label>
            <div class="control">
              <div class="select">
                <select v-model="formData.subject">
                  <option value="question">I want to ask a question</option>
                  <option value="book">I want to book a table</option>
                  <option value="problem">I have had a problem</option>
                </select>
              </div>
            </div>
          </div>          

          <div class="field">
            <label class="label">Your Message</label>
            <div class="control">
              <textarea class="textarea" placeholder="Write something..." v-model="formData.message"></textarea>
            </div>

            <p v-if="errors.message">
              <p class="help is-danger" v-for="error in errors.message" :key="error">{{ error }}</p>
            </p>
          </div>

          <div class="field is-grouped">
            <div class="control">
              <button class="button is-link" type="submit">Submit</button>
            </div>
            <div class="control">
              <button class="button is-link is-light" type="button" @click="handleClear">Clear</button>
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
  </Container>
</template>

<script>
import Vue from 'vue'
import validate from 'validate.js'
import * as r from 'ramda'
import { buildUrl } from '../utils/api'

const formData = {
  subject: 'question'
}

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
  message: {
    presence: true,
    length: {
      minimum: 3,
    }
  }
}

export default Vue.extend({
  data() {
    return {
      formData: Object.assign({}, formData),
      errors: [],
      submitting: false,
      submitError: false,
      submitSuccess: false,
    };
  },   
  methods: { 
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
        await this.$http.$post(buildUrl('contact'), this.formData)
        this.submitError = undefined
        this.submitSuccess = true
      } catch (e) {
        this.submitError = e
        this.submitSuccess = false
      }

      this.submitting = false
    }, 
    handleClear(e) {
      this.formData = Object.assign({}, formData)
    },
    hideSubmitStatus() {
      this.submitError = undefined
      this.submitSuccess = false
      this.submitting = false
    },
  }
})
</script>

<style>
</style>
