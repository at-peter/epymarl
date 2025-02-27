from .q_learner import QLearner
from .q_learner_coop import QLearnerCoop
from .coma_learner import COMALearner
from .qtran_learner import QLearner as QTranLearner
from .actor_critic_learner import ActorCriticLearner
from .maddpg_learner import MADDPGLearner
from .maddpg_learner_coop import MADDPGCoopLearner
from .ppo_learner import PPOLearner
from .ppo_coop_learner import PPOCoopLearner
from .actor_critic_coop_learner import ActorCriticCoopLearner


##### imports from the QTRAN code base
from .qtran_learner import QLearner as QTranLearner
#### imports from the QPLEX code base
from .qtran_learner import QLearner as QTranLearner
from .dmaq_qatten_learner import DMAQ_qattenLearner

##### imports from the FACMAC code base



REGISTRY = {}

REGISTRY["q_learner"] = QLearner
REGISTRY["q_learner_coop"] = QLearnerCoop
REGISTRY["coma_learner"] = COMALearner
REGISTRY["qtran_learner"] = QTranLearner
REGISTRY["actor_critic_learner"] = ActorCriticLearner
REGISTRY["actor_critic_coop_learner"] = ActorCriticCoopLearner
REGISTRY["maddpg_learner"] = MADDPGLearner
REGISTRY["ppo_learner"] = PPOLearner
REGISTRY["maddpg_coop_learner"] = MADDPGCoopLearner
REGISTRY["ppo_coop_learner"] = PPOCoopLearner

REGISTRY["qtran_learner"] = QTranLearner
REGISTRY["dmaq_qatten_learner"] = DMAQ_qattenLearner

