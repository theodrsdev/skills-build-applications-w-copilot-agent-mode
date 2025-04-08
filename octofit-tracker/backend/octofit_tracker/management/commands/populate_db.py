from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        users = [
            User(_id=ObjectId(), email='thundergod@mhigh.edu', name='Thor', age=30),
            User(_id=ObjectId(), email='metalgeek@mhigh.edu', name='Tony Stark', age=35),
            User(_id=ObjectId(), email='zerocool@mhigh.edu', name='Elliot Alderson', age=28),
            User(_id=ObjectId(), email='crashoverride@mhigh.edu', name='Dade Murphy', age=25),
            User(_id=ObjectId(), email='sleeptoken@mhigh.edu', name='Sleep Token', age=22),
        ]
        User.objects.bulk_create(users)

        # Create teams
        team1 = Team(_id=ObjectId(), name='Blue Team')
        team2 = Team(_id=ObjectId(), name='Gold Team')
        team1.save()
        team2.save()
        team1.members.add(users[0], users[1])
        team2.members.add(users[2], users[3], users[4])

        # Create activities
        activities = [
            Activity(_id=ObjectId(), user=users[0], activity_type='Cycling', duration=60, date='2025-04-08'),
            Activity(_id=ObjectId(), user=users[1], activity_type='Crossfit', duration=120, date='2025-04-07'),
            Activity(_id=ObjectId(), user=users[2], activity_type='Running', duration=90, date='2025-04-06'),
            Activity(_id=ObjectId(), user=users[3], activity_type='Strength', duration=30, date='2025-04-05'),
            Activity(_id=ObjectId(), user=users[4], activity_type='Swimming', duration=75, date='2025-04-04'),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(_id=ObjectId(), team=team1, points=200),
            Leaderboard(_id=ObjectId(), team=team2, points=300),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(_id=ObjectId(), name='Cycling Training', description='Training for a road cycling event'),
            Workout(_id=ObjectId(), name='Crossfit', description='Training for a crossfit competition'),
            Workout(_id=ObjectId(), name='Running Training', description='Training for a marathon'),
            Workout(_id=ObjectId(), name='Strength Training', description='Training for strength'),
            Workout(_id=ObjectId(), name='Swimming Training', description='Training for a swimming competition'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
