// StudentHomePage.jsx

import React, { useState, useEffect } from 'react';
import CourseCard from './CourseCard';
// You might need to import other components or hooks you will use

const StudentHomePage = () => {
  const [courses, setCourses] = useState([]);
  const [loading, setLoading] = useState(true);
  const studentId = "STUDENT_ID"; // This should come from the login session or state management

  useEffect(() => {
    // Fetch the courses the student is enrolled in
    const fetchCourses = async () => {
      try {
        setLoading(true);
        // Replace 'API_ENDPOINT' with your actual API endpoint to fetch courses
        const response = await fetch(`http://localhost:5000/courses/${studentId}`);
        const data = await response.json();
        setCourses(data);
      } catch (error) {
        console.error("Failed to fetch courses", error);
        // Handle error state here
      } finally {
        setLoading(false);
      }
    };

    fetchCourses();
  }, [studentId]);

  if (loading) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      {courses.map(course => (
        <CourseCard key={course.CourseId} course={course} />
      ))}
    </div>
  );
};

export default StudentHomePage;
