create database	IMDB;
use IMDB;

-- 1. Creating table movies
create table Movies (
	movie_id int primary key auto_increment,
    title varchar (30),
    director varchar (35),
    release_year year
);

insert into Movies (title, director, release_year)values 
('LEO', 'Lokesh', 2022),
('Master', 'Lokesh', 2024),
('Indian', 'Shankar', 2010);

select * from Movies;

-- 2. Creating media table:
create table Media (
	media_id int primary key auto_increment,
    movie_id int,
    media_type varchar (20),
    media_url varchar (100),
    foreign key (movie_id) references Movies(movie_id));

insert into Media (movie_id, media_type, media_url)values 
(1, 'Video', 'poster.mp4'),
(2, 'Image', 'pic.mpg');

select * from Media;

-- 3. Creating Genre table:
create table Genre (
	genre_id int primary key auto_increment,
    genre_name varchar(50));

insert into Genre (genre_name) values
('Romance'), ('thriller'),('crime'), ('historic'), ('comedy'), ('horror');

select * from Genre;

-- 4. Creating movie Genre table:
create table movie_genre (
	movie_id int,
    genre_id int,
    foreign key (movie_id) references Movies(movie_id),
    foreign key (genre_id) references Genre(genre_id)
);

insert into movie_genre values (1, 1),
(1, 2),(1, 4), (2,2) ,(3,1);

select * from movie_genre;

-- 5. Creating User table:
create table Users (
	user_id int primary key,
    user_name varchar (50));

insert into Users values
(101, 'Kaviya'),
(102, 'Karthik'),
(103, 'Mahe'),
(104, 'Padma');

select * from Users;

-- 6. Creating review table
create table Review (
	review_id int primary key,
    movie_id int,
    user_id int,
    rating int,
    comment text,
    foreign key (movie_id) references Movies(movie_id),
    foreign key (user_id) references Users(user_id));

insert into Review values
(1, 1, 101, 3, 'average'),
(2, 2, 102, 4, 'family-oriented'),
(3, 2, 103, 3, 'good');

select * from Review;

-- 7. Creating Artist table:
create table Artist (
	artist_id int primary key,
    artist_name varchar (100),
    industry varchar (100));
    
insert into Artist values
(1, 'Vijay', 'Kollywood'),
(2, 'Dhanush', 'Kollywood'),
(3, 'Ranveer', 'Bollywood');

select * from Artist;

-- 8. Creating Skills table:
create table Skills(
	skill_id int primary key,
    skill_name varchar (50));

insert into Skills values
(1, 'Dance'),
(2, 'Comedy'),
(3, 'Story-writing'),
(4, 'Director');

select * from Skills;

-- 9. creating artist skills table:
create table artist_skills(
	artist_id int,
    skill_id int,
    foreign key (artist_id) references Artist(artist_id),
    foreign key (skill_id) references Skills(skill_id)
);
insert into artist_skills values 
(1, 1), (1, 2), (1,3), (2, 1), (2, 3), (2, 4);

select * from artist_skills;

-- 10. creating roles table:
create table Roles(
	role_id int primary key auto_increment,
    role_name varchar(50));
    
insert into Roles values
(1, 'Hero'),
(2, 'Villain'),
(3, 'Comedian');

select * from Roles;

-- 11. creating artist movie role:

create table artist_movie_role (
	artist_id int,
    movie_id int,
    role_id int,
    primary key (artist_id, movie_id, role_id),
    foreign key (artist_id) references Artist(artist_id),
    foreign key (movie_id) references Movies(movie_id),
    foreign key (role_id) references Roles(role_id)
);

insert into artist_movie_role values
(1, 1, 1), (1, 2, 3), (2, 1, 3);

select * from artist_movie_role;

    
    

    
    
    
