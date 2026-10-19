from places import places


def recommend_places(budget, interests, available_time):

    recommendations = []

    normalized_interests = [
        str(interest).strip().lower()
        for interest in interests
    ]

    for place in places:

        if place["price"] > budget:
            continue

        if place["duration"] > available_time:
            continue

        place_tags = [
            str(tag).strip().lower()
            for tag in place["tags"]
        ]

        if normalized_interests:

            if not any(
                interest in place_tags
                for interest in normalized_interests
            ):
                continue

        recommendations.append(place)

    recommendations.sort(
        key=lambda place: (
            place["price"],
            place["duration"]
        )
    )

    return recommendations