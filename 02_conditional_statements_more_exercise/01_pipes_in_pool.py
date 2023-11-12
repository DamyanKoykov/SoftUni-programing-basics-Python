pool_capacity_ltr = float(input())
pipe_one_ltr_per_h = float(input())
pipe_two_ltr_per_h = float(input())
hours_worker_gone = float(input())

water_poured_pipe_one = pipe_one_ltr_per_h * hours_worker_gone
water_poured_pipe_two = pipe_two_ltr_per_h * hours_worker_gone
pipe_one_percent = (100 / (water_poured_pipe_one + water_poured_pipe_two)) * water_poured_pipe_one
pipe_two_percent = (100 / (water_poured_pipe_one + water_poured_pipe_two)) * water_poured_pipe_two
percent_of_pool_full = (100 / pool_capacity_ltr) * (water_poured_pipe_one + water_poured_pipe_two)
difference = ((pipe_one_ltr_per_h + pipe_two_ltr_per_h) * hours_worker_gone) - pool_capacity_ltr
if percent_of_pool_full <= 100:
    print(f"The pool is {percent_of_pool_full :.2f}% full. Pipe 1: \
{pipe_one_percent :.2f}%. Pipe 2: {pipe_two_percent :.2f}%.")
else:
    print(f"For {hours_worker_gone} hours the pool overflows with {difference} liters.")
