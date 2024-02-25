import React from 'react';
import { Card } from 'react-bootstrap';
// we might need to import other Bootstrap components or custom styles

const CourseCard = ({ course }) => {
  return (
    <Card style={{ width: '18rem', margin: '1rem' }}>
      <Card.Body>
        <Card.Title>{course.CourseName}</Card.Title>
        <Card.Text>
          {course.CourseDescription}
        </Card.Text>
        {/* This button will eventually link to the detailed course view */}
        <Card.Link href={`/courses/${course.CourseId}`}>View Details</Card.Link>
      </Card.Body>
    </Card>
  );
};

export default CourseCard;
