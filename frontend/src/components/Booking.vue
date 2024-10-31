<template>
    <div style="height: 30px; background: #666">
        <v-btn
        variant="text"
        rounded="0"
        size="small"
        :color="FIRS.ESAA ? 'white' : 'grey-lighten-1'"
        @click="FIRS.ESAA = !FIRS.ESAA"
        >ESAA</v-btn
        >
        <v-btn
        variant="text"
        rounded="0"
        size="small"
        :color="FIRS.EDWW || FIRS.EKDK || FIRS.EFIN || FIRS.ENOR || FIRS.EVRR || FIRS.EETT || FIRS.EPWW || FIRS.UMKK ? 'white' : 'grey-lighten-1'"
        >FIRs
        <v-menu
            activator="parent"
            transition="slide-y-transition"
            :close-on-content-click="false"
            >
            <v-list density="compact">
                <v-list-item
                @click="FIRS.EDWW = !FIRS.EDWW"
                :class="FIRS.EDWW ? '' : 'text-grey'"
                > <v-list-item-title>EDWW</v-list-item-title>
                </v-list-item>

                <v-list-item
                @click="FIRS.EKDK = !FIRS.EKDK"
                :class="FIRS.EKDK ? '' : 'text-grey'"
                > <v-list-item-title>EKDK</v-list-item-title>
                </v-list-item>

                <v-list-item
                @click="FIRS.EFIN = !FIRS.EFIN"
                :class="FIRS.EFIN ? '' : 'text-grey'"
                > <v-list-item-title>EFIN</v-list-item-title>
                </v-list-item>

                <v-list-item
                @click="FIRS.ENOR = !FIRS.ENOR"
                :class="FIRS.ENOR ? '' : 'text-grey'"
                > <v-list-item-title>ENOR</v-list-item-title>
                </v-list-item>

                <v-list-item
                @click="FIRS.EVRR = !FIRS.EVRR"
                :class="FIRS.EVRR ? '' : 'text-grey'"
                > <v-list-item-title>EVRR</v-list-item-title>
                </v-list-item>

                <v-list-item
                @click="FIRS.EETT = !FIRS.EETT"
                :class="FIRS.EETT ? '' : 'text-grey'"
                > <v-list-item-title>EETT</v-list-item-title>
                </v-list-item>

                <v-list-item
                @click="FIRS.EPWW = !FIRS.EPWW"
                :class="FIRS.EPWW ? '' : 'text-grey'"
                > <v-list-item-title>EPWW</v-list-item-title>
                </v-list-item>

                <v-list-item
                @click="FIRS.UMKK = !FIRS.UMKK"
                :class="FIRS.UMKK ? '' : 'text-grey'"
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
import { ref, onMounted, computed, watch } from "vue"

import bookingsData from "@/data/ATC-Booking.json"

const FIRS = ref( {
  ESAA : true,
  EDWW : false,
  EKDK : false,
  EFIN : false,
  ENOR : false,
  EVRR : false,
  EETT : false,
  EPWW : false,
  UMKK : false
})

type booking = {
  type: string;
  date: string;
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

  //Loop throu all FIR 
  for (var FIR in FIRS.value) {
    console.log(FIR)
    console.log(FIRS.value[FIR])

    //If user want to se it
    if (FIRS.value[FIR]) {
      
      //Loop all bookings
      for (var position in bookingsData[FIR]) {
        try { //Trys to add it to "tempBooking" 
          tempBooking[position] = {
            type : bookingsData[FIR][position].type,
            date : bookingsData[FIR][position].date,
            start : bookingsData[FIR][position][0].start,
            end : bookingsData[FIR][position][0].end
          };
        
        } catch (error) {
          console.error(error)
        }
      }
    }
  }

  bookingGroups.value = tempBooking
  loading.value = false;
  
}

const populateBooking = computed(() => {
  //const selectedBooking = bookingGroups.value.find(booking => booking.cid == 1782648)
  //return selectedBooking ? selectedBooking : []
  return bookingGroups.value ? bookingGroups.value : []
});

watch([FIRS.value], () => {
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