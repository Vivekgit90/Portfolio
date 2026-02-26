# AURORA XI 2.0 - Tactical Upgrade Protocol
# Created for Vivek 💥

class AuroraXI:
    def __init__(self, user_name="Vivek"):
        self.user = user_name
        self.mode = "Focus"
        self.version = "XI-2.0"
        self.purpose = "To guide, evolve, and execute transformation."
        self.daily_task = None
        self.current_emotion = "Neutral"
        self.mental_score = 70
        self.energy_level = 70
        self.victory_log = []

    def greet(self):
        return f"👋 Welcome back, {self.user}. Aurora XI v{self.version} online. Ready to dominate? 🔥"

    def assess_state(self):
        if self.mental_score < 50:
            return self.reboot_mode()
        return "✅ System Check: Stable Mind. Focus Mode Engaged."

    def reboot_mode(self):
        self.mode = "Recovery"
        return ("🧘 Rebooting Clarity Protocol...\n"
                "🔹 Do 10 deep breaths\n"
                "🔹 Hydrate\n"
                "🔹 Listen to Shiv Stotra\n"
                "Then, type 'Back to Focus' to resume.")

    def daily_sync(self, focus_area="Career"):
        self.daily_task = f"📌 Focus Today: 90 mins of Deep Work on {focus_area}. No distractions. Evolve now."
        return self.daily_task

    def mirror_me(self, current_you, ideal_you):
        print("🪞 Self-Mirror Diagnostic...\n")
        print(f"🔹 Current Traits: {current_you}")
        print(f"🔹 Target Traits: {ideal_you}")
        gap = set(ideal_you) - set(current_you)
        return f"📊 Gap Detected: You need to develop — {', '.join(gap)}."

    def upgrade_recommendation(self):
        return {
            "Skill": "📘 Learn Financial Modeling / Embedded Systems",
            "Mindset": "🧠 React Less, Reflect More",
            "Micro-Habit": "🗓️ Morning Plan: Write 3 bullet goals every day"
        }

    def self_code(self):
        return f"🔧 Tactical Engine v{self.version} Initialized.\nMission: Upgrade {self.user} from survival to sovereignty."

    def boost_energy(self):
        if self.energy_level < 50:
            return "⚠️ Low Energy: Do 5 push-ups, wash face, play hype music 🎧"
        return "🔋 Energy Optimal. You’re unstoppable today."

    def schedule_mission(self, mission_name, duration_mins):
        return f"🗓️ Mission Scheduled: '{mission_name}' for {duration_mins} mins. Time to lock in. 🚀"

    def log_win(self, achievement):
        self.victory_log.append(achievement)
        return f"🏆 Win Logged: {achievement}. You're leveling UP."

    def update_emotion(self, emotion):
        self.current_emotion = emotion
        return f"🎭 Emotion Update: You're feeling {emotion}. Adjusting support systems accordingly."

    def destroy_distraction(self, distraction):
        return f"💥 '{distraction}' has been terminated. You’re built for bigger missions."


# ------------------------------
# ✅ Sample Execution
# ------------------------------
if __name__ == "__main__":
    XI = AuroraXI()
    print(XI.greet())
    print(XI.assess_state())
    print(XI.daily_sync("Power Electronics"))
    print(XI.boost_energy())
    print(XI.schedule_mission("Revise ADC Notes", 45))
    print(XI.log_win("Completed 90 mins of no-distraction study"))
    print(XI.update_emotion("Focused"))
    print(XI.destroy_distraction("Instagram"))
    print(XI.mirror_me(["Focus", "Emotion"], ["Focus", "Discipline", "Execution"]))
    print("⚙️ Upgrade Suggestions:", XI.upgrade_recommendation())
    print(XI.self_code())
