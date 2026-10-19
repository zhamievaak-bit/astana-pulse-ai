from places import places


def recommend_places(budget, interests, available_time):

    recommendations = []

    for place in places:

        if place["price"] > budget:
            continue

        if place["duration"] > available_time:
            continue

        if interests:
            if not any(
                interest in place["tags"]
                for interest in interests
            ):
                continue

        recommendations.append(place)

    return recommendations