<template>
    <div style="height: 30px; background: #666">
        <v-btn
        variant="text"
        rounded="0"
        size="small"
        :color="ESAA ? 'white' : 'grey-lighten-1'"
        @click="ESAA = !ESAA"
        >ESAA</v-btn
        >
        <v-btn
        variant="text"
        rounded="0"
        size="small"
        :color="FIR.length > 0 ? 'white' : 'grey-lighten-1'"
        @click="adFilter = ''"
        >FIRs
        <v-menu
            activator="parent"
            transition="slide-y-transition"
            :close-on-content-click="false"
            >
            <v-list density="compact">
                <v-list-item
                @click="EDWW = !EDWW"
                :class="EDWW ? '' : 'text-grey'"
                > <v-list-item-title>EDWW</v-list-item-title>
                </v-list-item>

                <v-list-item
                @click="EKDK = !EKDK"
                :class="EKDK ? '' : 'text-grey'"
                > <v-list-item-title>EKDK</v-list-item-title>
                </v-list-item>

                <v-list-item
                @click="EFIN = !EFIN"
                :class="EFIN ? '' : 'text-grey'"
                > <v-list-item-title>EFIN</v-list-item-title>
                </v-list-item>

                <v-list-item
                @click="ENOR = !ENOR"
                :class="ENOR ? '' : 'text-grey'"
                > <v-list-item-title>ENOR</v-list-item-title>
                </v-list-item>

                <v-list-item
                @click="EVRR = !EVRR"
                :class="EVRR ? '' : 'text-grey'"
                > <v-list-item-title>EVRR</v-list-item-title>
                </v-list-item>

                <v-list-item
                @click="EETT = !EETT"
                :class="EETT ? '' : 'text-grey'"
                > <v-list-item-title>EETT</v-list-item-title>
                </v-list-item>

                <v-list-item
                @click="EPWW = !EPWW"
                :class="EPWW ? '' : 'text-grey'"
                > <v-list-item-title>EPWW</v-list-item-title>
                </v-list-item>

                <v-list-item
                @click="UMKK = !UMKK"
                :class="UMKK ? '' : 'text-grey'"
                > <v-list-item-title>UMKK</v-list-item-title>
                </v-list-item>
            </v-list>
        </v-menu>
        </v-btn>
        
    </div>
    <div>
      <div v-if="loading">Loading...</div>
      <div v-else-if="error">Error: {{ error }}</div>
      <div v-else class="card-grid">
        <v-card
        v-for="(group, index) in populateBooking"
        :key="index"
        class="direct-card"
        variant="outlined"
      >
        <div class="card-title">{{ index }}</div>
        <v-card-text>
          <div class="item-container">
              {{ group.start }}
              {{ group.end }}
          </div>
        </v-card-text>
      </v-card>
      </div>
  </div>
</template>

<script setup lang="ts">
import useEventBus from "@/eventbus"
import { ref, reactive, onMounted, computed, watch } from "vue"

import bookingsData from "@/data/ATC-Booking.json"
import type { ListFormat } from "typescript";

const ESAA = ref(true)
const EDWW = ref(false)
const EKDK = ref(false)
const EFIN = ref(false)
const ENOR = ref(false)
const EVRR = ref(false)
const EETT = ref(false)
const EPWW = ref(false)
const UMKK = ref(false)

const FIR = reactive(["ALL"])
const adFilter = ref("")

type booking = {
  type: string;
  start: string;
  end: string;
};

interface bookingDict<booking> {
  [position: string]: booking
}

const bookingGroups = ref<bookingDict<booking>>();
const loading = ref(true);
const error = ref<string | null>(null);

const loadBookings = () => {
  let tempBooking: bookingDict<booking> = {};

  if (ESAA.value) {
    for (var position in bookingsData['ESAA']) {
      try {
        tempBooking[position] = {
          type : bookingsData['ESAA'][position].type,
          start : bookingsData['ESAA'][position][0].start,
          end : bookingsData['ESAA'][position][0].end
        };
      
      } catch (error) {
        console.error(error)
      }
    }
  }
  bookingGroups.value = tempBooking
  console.log(tempBooking)
  loading.value = false;
  
}

const populateBooking = computed(() => {
  //const selectedBooking = bookingGroups.value.find(booking => booking.cid == 1782648)
  //return selectedBooking ? selectedBooking : []
  return bookingGroups.value ? bookingGroups.value : []
});

watch([ESAA, EDWW, EKDK, EFIN, ENOR, EVRR, EETT, EPWW, UMKK], () => {
  loadBookings()
})

onMounted(() => {
  loadBookings()

  // Set up event bus listener
  const bus = useEventBus();
  bus.on("refresh", () => {
    loadBookings()
    console.log("Refresh")
  });
});
</script>

<style scoped>
.card-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  padding: 10px;
}

.card-title {
  position: absolute;
  font-size: 0.9rem;
  z-index: 1;
  background-color: #dddddd;
  top: -10px;
  left: 8px;
  padding: 0 4px;
}

.direct-card {
  padding-top: 4px;
  flex: 1 1 175px;
  margin: 0;
  position: relative;
  overflow: visible !important;
}

.item-container {
  display: flex;
  flex-wrap: wrap;
  gap: 4px;
}

.item-chip {
  z-index: 2;
  font-size: 0.9rem;
  padding: 0 2px;
  height: 20px;
  min-width: 20px;
}

.v-card-text {
  padding: 6px;
}
</style>