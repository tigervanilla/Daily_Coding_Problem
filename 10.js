// Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

const jobScheduler = (f, n) => {
    setTimeout(f, n)
}

const f = (arg) => {
    console.log('f called')
}

jobScheduler(f, 1001)