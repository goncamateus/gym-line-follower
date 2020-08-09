from gym.envs.registration import register

register(
    id='LineFollower-v0',
    entry_point='gym_line_follower.envs:LineFollowerEnv',
    trials=10,
    reward_threshold=700
)

register(
    id='LineFollowerCamera-v0',
    entry_point='gym_line_follower.envs:LineFollowerCameraEnv',
    trials=10,
    reward_threshold=700
)

register(
    id='LineFollowerGoal-v0',
    entry_point='gym_line_follower.envs:LineFollowerGoalEnv',
    trials=10,
    reward_threshold=700
)
