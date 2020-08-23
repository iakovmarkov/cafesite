<template>
  <svg
    :viewBox="this.viewbox"
    class="waveContainer"
    xmlns="http://www.w3.org/2000/svg"
    xmlns:xlink="http://www.w3.org/1999/xlink"
    preserveAspectRatio="none"
    shape-rendering="auto"
  >
    <defs>
      <path id="path" d="M-160 44c30 0 58-18 88-18s 58 18 88 18 58-18 88-18 58 18 88 18 v44h-352z" />
      <linearGradient :id="getGradId" x1="0%" y1="0%" x2="0%" y2="50%">
        <stop
          v-for="item in this.gradient"
          :key="item.offset"
          :offset="item.offset"
          :style="item.style"
        />
      </linearGradient>
    </defs>
    <!-- I have to apply class and style to g instead of use, because it's better supported in FF -->
    <g class="wave" :style="cssVars">
      <use xlink:href="#path" x="0" y="0" :fill="getFill" />
    </g>
  </svg>
</template>

<script>
export default {
  props: {
    viewbox: String,
    gradient: Array,
    duration: Number,
    direction: String,
    fuzz: {
      // The only way to control animation from component props.
      type: [Number, String],
      default: 11,
    }
  },
  computed: {
    getGradId() {
      return `gradient_${this._uid}`
    },
    getFill() {
      return `url(#gradient_${this._uid})`
    },
    cssVars() {
      return {
        '--delay': `${Number(this.fuzz) * -5}ms`,
        '--direction': this.direction,
        '--duration': `${(this.duration || 3000) + Number(this.fuzz) * 10}ms`,
      }
    },
  },
}
</script>

<style scoped>
.waveContainer {
  height: 100%;
  width: 100%;
  position: absolute;
  top: 0;
  left: 0;
  z-index: 999;
}

.waveContainer:nth-child(2) {
  top: 50%;
}

.wave use {
  width: 100%;
  animation-name: psychWave;
  animation-timing-function: linear;
  animation-iteration-count: infinite;
  animation-duration: var(--duration);
  animation-direction: var(--direction);
  animation-delay: var(--delay);
}

@keyframes psychWave {
  0% {
    transform: translateX(-90px);
  }
  100% {
    transform: translateX(85px);
  }
}
</style>