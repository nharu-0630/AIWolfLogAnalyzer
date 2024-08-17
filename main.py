import csv
import os

team_role_win = dict()
team_role_nums = dict()
file_paths = []
for root, dirs, files in os.walk("./JP2/"):
    for file in sorted(files):
        if "dummy" in file:
            print(f"Skipping {file} due to dummy player")
            continue
        if file.endswith(".log"):
            file_paths.append(os.path.join(root, file))
            print(f"Added {file} to list")

for file_path in file_paths:
    team_role = dict()
    win_side = None
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            values = line.split(",")
            if values[0] == "0" and values[1] == "status":
                team = values[5].strip()
                team = team.rstrip("0123456789")
                team_role[team] = values[3].strip()
            if values[1] == "result":
                win_side = values[4].strip()
                break
    if win_side is None:
        print(f"Skipping {file_path} due to missing win side")
        continue
    if "dummy" in team_role:
        print(f"Skipping {file_path} due to dummy player")
        continue
    for team, role in team_role.items():
        if team not in team_role_win:
            team_role_win[team] = dict()
        if role not in team_role_win[team]:
            team_role_win[team][role] = 0
        if team not in team_role_nums:
            team_role_nums[team] = dict()
        if role not in team_role_nums[team]:
            team_role_nums[team][role] = 0
        team_role_nums[team][role] += 1
        if win_side == "VILLAGER" and role != "WEREWOLF" and role != "POSSESSED":
            team_role_win[team][role] += 1
        elif win_side == "WEREWOLF" and (role == "WEREWOLF" or role == "POSSESSED"):
            team_role_win[team][role] += 1

roles = sorted(set(role for role_win in team_role_win.values() for role in role_win))

header = (
    ["Team"]
    + [f"{role} Total Games" for role in roles]
    + [f"{role} Win Rate (%)" for role in roles]
    + [
        "Total Wins",
        "Total Games",
        "Win Rate (%)",
        "Average Win Rate (%)",
        "Average Win Rate (%) (Villager Win Rate Doubled)",
    ]
)

with open("team_role_stats.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)

    for team, roles_dict in team_role_nums.items():
        row = [team]
        for role in roles:
            total_games = team_role_nums[team].get(role, 0)
            win_rate = (
                (team_role_win[team].get(role, 0) / total_games * 100)
                if total_games > 0
                else 0
            )
            row.append(total_games)
        for role in roles:
            total_games = team_role_nums[team].get(role, 0)
            win_rate = (
                (team_role_win[team].get(role, 0) / total_games * 100)
                if total_games > 0
                else 0
            )
            row.append(f"{win_rate:04.2f}")

        # Calculate total wins, total games, and overall win rate
        total_wins = sum(team_role_win[team].values())
        total_games = sum(team_role_nums[team].values())
        overall_win_rate = (total_wins / total_games) * 100 if total_games > 0 else 0
        row.extend([total_wins, total_games, f"{overall_win_rate:04.2f}"])

        # Calculate average win rate
        total_win_rate = 0
        total_roles = len(team_role_win[team])
        for role, win in team_role_win[team].items():
            total_games = team_role_nums[team][role]
            win_rate = (win / total_games) * 100
            total_win_rate += win_rate
        average_win_rate = total_win_rate / total_roles if total_roles > 0 else 0
        row.append(f"{average_win_rate:04.2f}")

        # Calculate average win rate with villagers' win rate doubled
        total_win_rate_doubled = 0
        for role, win in team_role_win[team].items():
            total_games = team_role_nums[team][role]
            win_rate = (win / total_games) * 100
            weight = 2 if role == "VILLAGER" else 1
            total_win_rate_doubled += win_rate * weight
        average_win_rate_doubled = total_win_rate_doubled / sum(
            2 if role == "VILLAGER" else 1 for role in team_role_win[team].keys()
        )
        row.append(f"{average_win_rate_doubled:04.2f}")

        writer.writerow(row)
