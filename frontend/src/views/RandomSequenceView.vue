<template>
  <div id="random-sequence-view">
    <RandomSequenceComponent msg="Generate random sequence"/>
  </div>
</template>

<script>
import RandomSequenceComponent from "@/components/RandomSequenceComponent.vue"

export default {
  name: "RandomSequenceView",
  components: { RandomSequenceComponent, }
}
</script>
